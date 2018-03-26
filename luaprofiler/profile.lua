-- define module
local profiler = {}

-- load modules

local stringFormat = string.format
local table_insert = table.insert
local table_remove = table.remove

local getUSTick = os.clock


local stack_table = {}

stack_table.push =  function(item)
    if stack_table.items == nil then
        stack_table.items ={}
    end
    local size = #stack_table.items
    stack_table.items[size+1] = item
end
stack_table.pop = function ()
  
    if  stack_table.items == nil then
        return nil
    end
    local size = #stack_table.items
    local item =  stack_table.items[size]
    stack_table.items[size] = nil
    return item
end

-- get the function title
function profiler:_func_title(funcinfo)
    -- the function name
    local name = funcinfo.name or 'anonymous'
    -- the function line
    local line = stringFormat("%d", funcinfo.linedefined or 0)
    -- the function source
    local source = funcinfo.short_src or 'C_FUNC'
    -- make title
    return stringFormat("%-30s: %s: %s", name, source, line)
end

-- get the function report
function profiler:_func_report(funcinfo)
    -- get the function title
    local title = profiler:_func_title(funcinfo)
    -- get the function report
    local report = self._REPORTS_BY_TITLE[title]
    if not report then
        -- init report
        report = 
        {
            title       = self:_func_title(funcinfo)
        ,   callcount   = 0
        ,   totaltime   = 0
        }

        -- save it
        self._REPORTS_BY_TITLE[title] = report
        table_insert(self._REPORTS, report)
    end

    -- ok?
    return report
end

-- profiling call
function profiler:_profiling_call(funcinfo)

    -- get the function report
    local report = self:_func_report(funcinfo)
 
    -- save the call time
    report.calltime  =  getUSTick()
    -- if funcinfo.istailcall then
    --     print(stringFormat("tail call:%s",self:_func_title(funcinfo)))
    -- else
    --     print(stringFormat("call:%s",self:_func_title(funcinfo)))
    -- end

end

-- profiling return
function profiler:_profiling_return(funcinfo)
   
    -- get the stoptime
    local stoptime = getUSTick()
    -- get the function report
    local report = self:_func_report(funcinfo)
    assert(report)
    -- update the call count
    report.callcount   = report.callcount + 1
    -- update the total time
    if report.calltime and report.calltime > 0 then
        report.totaltime = report.totaltime + (stoptime - report.calltime)
        report.calltime = 0
    end
    -- if funcinfo.istailcall then
    --     print(stringFormat("tail return:%s",self:_func_title(funcinfo)))
    -- else
    --     print(stringFormat("return:%s",self:_func_title(funcinfo)))
    -- end
    -- check tail call 
    if funcinfo.istailcall  then
        local stack = stack_table.pop()
        if stack then
            return profiler:_profiling_return(stack)
        end
    end
   
end

-- the profiling handler
function profiler._profiling_handler(hooktype)

    -- the function info
    local funcinfo = debug.getinfo(2, 'ntlS')

    -- dispatch it
    if hooktype == "call" or hooktype == "tail call" then
        stack_table.push(funcinfo)
        profiler:_profiling_call(funcinfo)
    elseif hooktype == "return"   then
        stack_table.pop()
        profiler:_profiling_return(funcinfo)
    end
end


-- start profiling
function profiler:start(fileName)

	-- init reports
	self.logFile = io.open(fileName, "w+")
	if not self.logFile then return false end
	
	self._REPORTS           = {}
	self._REPORTS_BY_TITLE  = {}

	-- save the start time
	self._STARTIME = getUSTick()

	-- start to hook
	debug.sethook(profiler._profiling_handler, 'cr', 0)
    return true
end

-- stop profiling
function profiler:stop()
	local logFile = self.logFile
	if not logFile then return false end
	-- save the stop time
	self._STOPTIME = getUSTick()

	-- stop to hook
	debug.sethook()

	-- calculate the total time 
	local totaltime = self._STOPTIME - self._STARTIME

	-- sort reports
	table.sort(self._REPORTS, function(a, b)
		return a.totaltime > b.totaltime
	end)

	-- show reports
	for _, report in ipairs(self._REPORTS) do
		
		-- calculate percent
		local percent = (report.totaltime / totaltime) * 100
		if percent < 1 then
			break
		end
		logFile:write(stringFormat("%6.3f, %6.2f%%, %7d, %6.3f, %s\r\n", report.totaltime, percent, report.callcount, report.totaltime/report.callcount, report.title))
	
	end
	logFile:close()
	logFile = nil
end

-- return module
return profiler
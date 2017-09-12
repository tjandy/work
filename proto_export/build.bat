proto\bin\protoc.exe --java_out=java --csharp_out=csharp --python_out=python msg.proto

python genMessageID.py msg.proto

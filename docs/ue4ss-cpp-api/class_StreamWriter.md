# StreamWriter

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/USMapGenerator/writer.h`
Kind: class

## Members

### ~StreamWriter()
### FORCEINLINE std::stringstream & GetBuffer()
### FORCEINLINE void WriteString(std::string String) override
### FORCEINLINE void WriteString(std::string_view String) override
### FORCEINLINE void Write(void *Input, size_t Size) override
### FORCEINLINE void Seek(int Pos, int Origin=SEEK_CUR) override
### uint32_t Size() override
### FORCEINLINE void Write(T Input)

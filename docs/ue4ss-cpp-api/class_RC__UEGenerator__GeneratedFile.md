# RC::UEGenerator::GeneratedFile

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/SDKGenerator/UEHeaderGenerator.hpp`
Kind: class

## Members

### GeneratedFile(const FFilePath &full_file_path)
### ~GeneratedFile()=default
### GeneratedFile(const GeneratedFile &)=delete
### GeneratedFile(GeneratedFile &&)=default
### auto operator=(const GeneratedFile &) -> void=delete
### auto append_line(const StringType &line) -> void
### auto append_line_no_indent(const StringType &line) -> void
### auto begin_indent_level() -> void
### auto end_indent_level() -> void
### auto serialize_file_content_to_disk() -> bool
### auto has_content_to_save() const -> bool
### auto generate_file_contents() -> StringType

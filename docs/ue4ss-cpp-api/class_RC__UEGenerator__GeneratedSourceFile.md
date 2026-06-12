# RC::UEGenerator::GeneratedSourceFile

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/SDKGenerator/UEHeaderGenerator.hpp`
Kind: class

## Members

### variable StringType m_implementation_constructor
### variable std::unordered_set< StringType > parent_property_names
### variable std::map< FProperty *, std::tuple< StringType, StringType, bool > > attachments
### GeneratedSourceFile(const FFilePath &file_path, const StringType &file_module_name, bool is_implementation_file, UObject *object)
### GeneratedSourceFile(const GeneratedSourceFile &)=delete
### GeneratedSourceFile(GeneratedSourceFile &&)=default
### auto operator=(const GeneratedSourceFile &) -> void=delete
### auto set_header_file(GeneratedSourceFile *header_file) -> void
### auto add_dependency_object(UObject *object, DependencyLevel dependency_level) -> void
### auto add_extra_include(const StringType &included_file_name) -> void
### auto get_header_module_name() const -> const StringType &
### auto is_implementation_file() const -> bool
### auto get_current_string_position() -> size_t
### auto set_need_get_type_hash(bool new_value) -> void
### auto get_corresponding_object() -> UObject *
### auto has_content_to_save() const -> bool override
### auto copy_dependency_module_names(std::set< StringType > &out_dependency_module_names) const -> void
### auto generate_file_contents() -> StringType override
### auto create_source_file(const FFilePath &root_dir, const StringType &module_name, const StringType &base_name, bool is_implementation_file, UObject *object) -> GeneratedSourceFile

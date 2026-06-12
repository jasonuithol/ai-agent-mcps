# RC::UEGenerator::UEHeaderGenerator

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/SDKGenerator/UEHeaderGenerator.hpp`
Kind: class

## Members

### UEHeaderGenerator(const FFilePath &root_directory)
### UEHeaderGenerator(const UEHeaderGenerator &)=delete
### UEHeaderGenerator(UEHeaderGenerator &&)=delete
### auto operator=(const UEHeaderGenerator &) -> void=delete
### auto ignore_selected_modules() -> void
### auto dump_native_packages() -> void
### auto generate_object_description_file(UObject *object) -> bool
### auto generate_module_build_file(const StringType &module_name) -> void
### auto generate_module_implementation_file(const StringType &module_name) -> void
### auto add_module_and_sub_module_dependencies(std::set< StringType > &out_module_dependencies, const StringType &module_name, bool add_self_module=true) -> void
### auto collect_blacklisted_property_names(UObject *property) -> CaseInsensitiveSet
### auto generate_object_pre_declaration(UObject *object) -> std::vector< std::vector< StringType > >
### auto convert_module_name_to_api_name(const StringType &module_name) -> StringType
### auto get_module_name_for_package(UObject *package) -> StringType
### auto sanitize_enumeration_name(const StringType &enumeration_name) -> StringType
### auto get_highest_enum(UEnum *uenum) -> int64_t
### auto get_lowest_enum(UEnum *uenum) -> int64_t
### auto get_class_blueprint_info(UClass *function) -> ClassBlueprintInfo
### auto is_struct_blueprint_type(UScriptStruct *property) -> bool
### auto is_function_parameter_shadowing(UClass *property, FProperty *function_parameter) -> bool
### auto append_access_modifier(GeneratedSourceFile &header_data, AccessModifier needed_access, AccessModifier &current_access) -> void
### auto get_property_access_modifier(FProperty *property) -> AccessModifier
### auto get_function_access_modifier(UFunction *function) -> AccessModifier
### auto create_string_literal(const StringType &string) -> StringType
### auto create_utf8_string_literal(const StringType &string) -> StringType
### auto create_ansi_string_literal(const StringType &string) -> StringType
### auto get_header_name_for_object(UObject *object, bool get_existing_header=false) -> StringType
### auto generate_cross_module_include(UObject *object, const StringType &module_name, const StringType &fallback_name) -> StringType

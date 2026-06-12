# RC::UEGenerator

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/SDKGenerator/Common.hpp`
Kind: namespace

## Members

### enum DelegateType

- `Delegate`
- `MulticastInlineDelegate`
- `MulticastSparseDelegate`
### enum EnableForwardDeclarations

- `Yes`
- `No`
### enum IsDelegateFunction

- `Yes`
- `No`
### enum DependencyLevel

- `NoDependency`
- `PreDeclaration` — Object dependency will result in a pre-declaration statement generation.
- `Include` — Object dependency will result in the header include generation.
### enum AccessModifier

- `None`
- `Public`
- `Protected`
- `Private`
### typedef std::filesystem::path FFilePath
### typedef RC::Unreal::UObject UObject
### typedef RC::Unreal::UStruct UStruct
### typedef RC::Unreal::UClass UClass
### typedef RC::Unreal::FProperty FProperty
### typedef RC::Unreal::FField FField
### typedef RC::Unreal::UEnum UEnum
### typedef RC::Unreal::UScriptStruct UScriptStruct
### typedef RC::Unreal::UFunction UFunction
### typedef std::set< StringType, StringInsensitiveCompare > CaseInsensitiveSet
### auto is_integral_type(Unreal::FProperty *property) -> bool
### auto get_native_enum_name(Unreal::UEnum *uenum, bool include_type=true) -> File::StringType
### auto generate_property_cxx_name(Unreal::FProperty *property, bool is_top_level_declaration, Unreal::UObject *class_context, EnableForwardDeclarations=EnableForwardDeclarations::No) -> File::StringType
### auto generate_property_lua_name(Unreal::FProperty *property, bool is_top_level_declaration, Unreal::UObject *class_context) -> File::StringType
### auto sanitize_property_name(const File::StringType &property_name) -> File::StringType
### auto generate_delegate_name(Unreal::FProperty *property, const File::StringType &context_name) -> File::StringType
### auto get_native_class_name(Unreal::UClass *uclass, bool interface_name=false) -> File::StringType
### auto get_native_struct_name(Unreal::UScriptStruct *script_struct) -> File::StringType
### auto get_native_delegate_type_name(Unreal::UFunction *signature_function, Unreal::UClass *current_class=nullptr, bool strip_outer_name=false) -> File::StringType
### auto is_delegate_signature_function(Unreal::UFunction *signature_function) -> bool
### auto strip_delegate_signature_postfix(Unreal::UFunction *signature_function) -> File::StringType
### auto generate_cxx_headers(const std::filesystem::path directory_to_generate_in) -> void
### auto generate_lua_types(const std::filesystem::path directory_to_generate_in) -> void

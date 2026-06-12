# RC::ObjectDumper

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/ObjectDumper/ObjectToString.hpp`
Kind: namespace

## Members

### typedef size_t ToStringHash
### typedef std::function< void(void *, StringType &)> ObjectToStringDecl
### typedef const std::function< void(void *)> & ObjectToStringComplexDeclCallable
### typedef std::function< void(void *, File::StringType &, ObjectToStringComplexDeclCallable)> ObjectToStringComplexDecl
### variable std::unordered_map< ToStringHash, ObjectToStringDecl > object_to_string_functions
### variable std::unordered_map< ToStringHash, ObjectToStringComplexDecl > object_to_string_complex_functions
### auto get_to_string(size_t hash) -> ObjectToStringDecl
### auto get_to_string_complex(size_t hash) -> ObjectToStringComplexDecl
### auto to_string_exists(size_t hash) -> bool
### auto to_string_complex_exists(size_t hash) -> bool
### auto object_trivial_dump_to_string(void *p_this, StringType &out_line, const CharType *post_delimiter=STR(".")) -> void
### auto object_to_string(void *p_this, StringType &out_line) -> void
### auto property_trivial_dump_to_string(void *p_this, StringType &out_line) -> void
### auto property_to_string(void *p_this, StringType &out_line) -> void
### auto arrayproperty_to_string(void *p_this, StringType &out_line) -> void
### auto arrayproperty_to_string_complex(void *p_this, StringType &out_line, ObjectToStringComplexDeclCallable callable) -> void
### auto mapproperty_to_string(void *p_this, StringType &out_line) -> void
### auto mapproperty_to_string_complex(void *p_this, StringType &out_line, ObjectToStringComplexDeclCallable callable) -> void
### auto classproperty_to_string(void *p_this, StringType &out_line) -> void
### auto delegateproperty_to_string(void *p_this, StringType &out_line) -> void
### auto fieldpathproperty_to_string(void *p_this, StringType &out_line) -> void
### auto interfaceproperty_to_string(void *p_this, StringType &out_line) -> void
### auto multicastdelegateproperty_to_string(void *p_this, StringType &out_line) -> void
### auto objectproperty_to_string(void *p_this, StringType &out_line) -> void
### auto structproperty_to_string(void *p_this, StringType &out_line) -> void
### auto enumproperty_to_string(void *p_this, StringType &out_line) -> void
### auto boolproperty_to_string(void *p_this, StringType &out_line) -> void
### auto enum_to_string(void *p_this, StringType &out_line) -> void
### auto struct_to_string(void *p_this, StringType &out_line) -> void
### auto function_to_string(void *p_this, StringType &out_line, std::unordered_set< Unreal::UFunction * > *in_dumped_functions) -> void
### auto scriptstruct_to_string_complex(void *p_this, StringType &out_line, ObjectToStringComplexDeclCallable callable) -> void
### auto dump_xproperty(Unreal::FProperty *property, StringType &out_line) -> void
### auto init() -> void

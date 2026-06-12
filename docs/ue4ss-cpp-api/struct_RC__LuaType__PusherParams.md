# RC::LuaType::PusherParams

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaUObject.hpp`
Kind: struct

## Members

### variable const Operation operation
### variable const LuaMadeSimple::Lua & lua
### variable Unreal::UObject * base
### variable void * data
### variable Unreal::FProperty * property
### variable int32_t stored_at_index
### variable bool create_new_if_get_non_trivial_local
### auto get_operation() const -> const char *
### auto get_stack_dump(const char *message="") const -> std::string
### auto throw_error_internal_append_args(std::string &) const -> void
### auto throw_error_internal_append_args(std::string &error_message, K1 &&key, V1 &&value) const -> void
### auto throw_error_internal_append_args(std::string &error_message, K1 &&key, V1 &&value, Remaining &&... remaining) const -> void
### auto throw_error(std::string_view handler_name, std::string_view format, Args &&... args) const -> void

# RC::CppMod

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/Mod/CppMod.hpp`
Kind: class

## Members

### CppMod(UE4SSProgram &, StringType &&mod_name, StringType &&mod_path)
### CppMod(CppMod &)=delete
### CppMod(CppMod &&)=delete
### ~CppMod() override
### auto start_mod() -> void override
### auto uninstall() -> void override
### auto fire_on_lua_start(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
### auto fire_on_lua_start(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
### auto fire_on_lua_stop(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
### auto fire_on_lua_stop(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
### auto fire_unreal_init() -> void override
### auto fire_ui_init() -> void override
### auto fire_program_start() -> void override
### auto fire_update() -> void override
### auto fire_dll_load(StringViewType dll_name) -> void
### auto fire_on_cpp_mods_loaded() -> void

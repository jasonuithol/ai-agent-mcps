# RC::CppUserModBase

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/Mod/CppUserModBase.hpp`
Kind: class

## Members

### variable StringType ModName
### variable StringType ModVersion
### variable StringType ModDescription
### variable StringType ModAuthors
### variable StringType ModIntendedSDKVersion
### CppUserModBase()
### ~CppUserModBase()
### auto on_update() -> void
### auto on_unreal_init() -> void
### auto on_ui_init() -> void
### auto on_program_start() -> void
### auto on_lua_start(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, std::vector< LuaMadeSimple::Lua * > &hook_luas) -> void
Executes after a Lua mod is started (DEPRECATED).
DeprecatedUse the overload with LuaMadeSimple::Lua* hook_lua instead. This overload may be removed in the next release. mod_name This is the name of the Lua mod that was started. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_luas DEPRECATED: This container previously held multiple hook Lua instances. Now only one hook instance is used.
### auto on_lua_start(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, std::vector< LuaMadeSimple::Lua * > &hook_luas) -> void
Executes after a Lua mod of the same name is started (DEPRECATED).
DeprecatedUse the overload with LuaMadeSimple::Lua* hook_lua instead. This overload may be removed in the next release. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_luas DEPRECATED: This container previously held multiple hook Lua instances. Now only one hook instance is used.
### auto on_lua_stop(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, std::vector< LuaMadeSimple::Lua * > &hook_luas) -> void
Executes before a Lua mod is about to be stopped (DEPRECATED).
DeprecatedUse the overload with LuaMadeSimple::Lua* hook_lua instead. This overload may be removed in the next release. mod_name This is the name of the Lua mod that is about to be stopped. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_luas DEPRECATED: This container previously held multiple hook Lua instances. Now only one hook instance is used.
### auto on_lua_stop(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, std::vector< LuaMadeSimple::Lua * > &hook_luas) -> void
Executes before a Lua mod of the same name is about to be stopped (DEPRECATED).
DeprecatedUse the overload with LuaMadeSimple::Lua* hook_lua instead. This overload may be removed in the next release. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_luas DEPRECATED: This container previously held multiple hook Lua instances. Now only one hook instance is used.
### auto on_dll_load(StringViewType dll_name) -> void
### auto render_tab() -> void
### auto on_lua_start(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
Executes after a Lua mod is started.
Executes for every Lua mod that is starting. mod_name This is the name of the Lua mod that was started. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_lua This is the Lua instance that is used for game-thread hooks like ExecuteInGameThread.
### auto on_lua_start(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
Executes after a Lua mod of the same name is started.
lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_lua This is the Lua instance that is used for game-thread hooks like ExecuteInGameThread.
### auto on_lua_stop(StringViewType mod_name, LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
Executes before a Lua mod is about to be stopped.
Executes for every Lua mod that is stopping. mod_name This is the name of the Lua mod that is about to be stopped. lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_lua This is the Lua instance that is used for game-thread hooks like ExecuteInGameThread.
### auto on_lua_stop(LuaMadeSimple::Lua &lua, LuaMadeSimple::Lua &main_lua, LuaMadeSimple::Lua &async_lua, LuaMadeSimple::Lua *hook_lua) -> void
Executes before a Lua mod of the same name is about to be stopped.
lua This is the main Lua instance. main_lua This is the main Lua thread instance. async_lua This is the Lua instance for asynchronous things like ExecuteAsync and ExecuteWithDelay. hook_lua This is the Lua instance that is used for game-thread hooks like ExecuteInGameThread.
### auto on_cpp_mods_loaded() -> void
Executes after every C++ mod has been loaded.

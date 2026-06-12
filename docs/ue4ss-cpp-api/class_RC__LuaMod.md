# RC::LuaMod

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/Mod/LuaMod.hpp`
Kind: class

## Members

### enum ActionType

- `Immediate`
- `Delayed`
- `Loop`
### enum DelayedActionStatus

- `Pending`
- `Active`
- `Paused`
- `Executing`
- `PendingRemoval`
### variable LuaMadeSimple::Lua * m_hook_lua
### variable LuaMadeSimple::Lua * m_main_lua
### variable LuaMadeSimple::Lua * m_async_lua
### variable std::vector< AsyncAction > m_pending_actions
### variable std::vector< AsyncAction > m_delayed_actions
### variable int64_t m_next_delayed_action_handle
### variable std::vector< LuaCancellableCallbackData > m_static_construct_object_lua_callbacks
### variable uint64_t m_next_static_construct_callback_id
### variable std::vector< LuaCallbackData > m_process_console_exec_pre_callbacks
### variable std::vector< LuaCallbackData > m_process_console_exec_post_callbacks
### variable std::vector< LuaCallbackData > m_call_function_by_name_with_arguments_pre_callbacks
### variable std::vector< LuaCallbackData > m_call_function_by_name_with_arguments_post_callbacks
### variable std::vector< LuaCallbackData > m_local_player_exec_pre_callbacks
### variable std::vector< LuaCallbackData > m_local_player_exec_post_callbacks
### variable std::unordered_map< File::StringType, LuaCallbackData > m_global_command_lua_callbacks
### variable std::unordered_map< File::StringType, LuaCallbackData > m_custom_command_lua_pre_callbacks
### variable std::vector< SimpleLuaAction > m_game_thread_actions
### variable std::vector< SimpleLuaAction > m_engine_tick_actions
### variable std::vector< DelayedGameThreadAction > m_delayed_game_thread_actions
### variable std::vector< SimpleLuaAction > m_pending_game_thread_actions
### variable std::vector< SimpleLuaAction > m_pending_engine_tick_actions
### variable std::vector< DelayedGameThreadAction > m_pending_delayed_game_thread_actions
### variable std::vector< PendingNotifyOnNewObjectCallback > m_pending_notify_on_new_object_callbacks
### variable bool m_is_processing_actions
### variable GameThreadExecutionMethod m_default_game_thread_method
### variable std::unordered_map< std::string, SharedLuaVariable > m_shared_lua_variables
### variable std::vector< FunctionHookData > m_custom_event_callbacks
### variable std::vector< LuaCallbackData > m_load_map_pre_callbacks
### variable std::vector< LuaCallbackData > m_load_map_post_callbacks
### variable std::vector< LuaCallbackData > m_init_game_state_pre_callbacks
### variable std::vector< LuaCallbackData > m_init_game_state_post_callbacks
### variable std::vector< LuaCallbackData > m_begin_play_pre_callbacks
### variable std::vector< LuaCallbackData > m_begin_play_post_callbacks
### variable std::vector< LuaCallbackData > m_end_play_pre_callbacks
### variable std::vector< LuaCallbackData > m_end_play_post_callbacks
### variable std::vector< FunctionHookData > m_script_hook_callbacks
### variable bool m_is_currently_executing_game_action
### variable std::recursive_mutex m_thread_actions_mutex
### LuaMod(UE4SSProgram &, StringType &&mod_name, StringType &&mod_path)
### ~LuaMod() override=default
### auto start_mod() -> void override
### auto uninstall() -> void override
### auto prepare_mod(const LuaMadeSimple::Lua &lua) -> void
### auto lua() const -> const LuaMadeSimple::Lua &
### auto main_lua() const -> const LuaMadeSimple::Lua *
### auto async_lua() const -> const LuaMadeSimple::Lua *
### auto get_lua_state() const -> lua_State *
### auto get_scripts_path() const -> const std::filesystem::path &
### auto actions_lock() -> void
### auto actions_unlock() -> void
### auto get_async_thread_id() const -> std::thread::id
### auto get_main_thread_id() const -> std::thread::id
### auto update_async() -> void override
### auto process_delayed_actions() -> void
### auto clear_delayed_actions() -> void
### auto on_program_start() -> void
### auto global_uninstall() -> void
### auto get_object_names(const Unreal::UObject *) -> std::vector< Unreal::FName >
### auto find_function_hook_data(std::vector< FunctionHookData > &, Unreal::FName) -> FunctionHookData *
### auto find_function_hook_data(std::vector< FunctionHookData > &, const Unreal::UObject *) -> FunctionHookData *
### auto find_function_hook_data(std::vector< FunctionHookData > &, const std::vector< Unreal::FName > &) -> FunctionHookData *
### auto remove_function_hook_data(std::vector< FunctionHookData > &, StringViewType) -> void
### auto remove_function_hook_data(std::vector< FunctionHookData > &, Unreal::FName) -> void
### auto remove_function_hook_data(std::vector< FunctionHookData > &, const Unreal::UObject *) -> void
### auto remove_function_hook_data(std::vector< FunctionHookData > &, const std::vector< Unreal::FName > &) -> void

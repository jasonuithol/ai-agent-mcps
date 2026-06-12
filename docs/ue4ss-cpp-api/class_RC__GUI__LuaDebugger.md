# RC::GUI::LuaDebugger

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/LuaDebugger.hpp`
Kind: class

## Members

### variable constexpr size_t MAX_ERROR_HISTORY
### variable constexpr size_t MAX_STACK_PREVIEW_LENGTH
### variable constexpr size_t MAX_REPL_HISTORY
### variable constexpr size_t MAX_TABLE_DEPTH
### LuaDebugger()
### ~LuaDebugger()
### auto register_lua_state(lua_State *L, const std::string &mod_name, const std::string &state_type) -> void
### auto unregister_lua_state(lua_State *L) -> void
### auto update_state_stack(lua_State *L) -> void
### auto record_error(lua_State *L, const std::string &error_message, const std::string &traceback) -> void
### auto clear_error_history() -> void
### auto get_error_count() const -> size_t
### auto add_breakpoint(const std::string &source, int line, const std::string &condition="") -> void
### auto remove_breakpoint(const std::string &source, int line) -> void
### auto toggle_breakpoint(const std::string &source, int line) -> void
### auto clear_all_breakpoints() -> void
### auto has_breakpoint(const std::string &source, int line) const -> bool
### auto is_paused() const -> bool
### auto continue_execution() -> void
### auto step_into() -> void
### auto step_over() -> void
### auto step_out() -> void
### auto install_debug_hook(lua_State *L) -> void
### auto uninstall_debug_hook(lua_State *L) -> void
### auto has_debug_hook(lua_State *L) const -> bool
### auto load_script(const std::string &path) -> const LuaScriptFile *
### auto get_mod_scripts(lua_State *L) -> std::vector< std::string >
### auto save_script(const std::string &path, const std::string &content) -> bool
### auto reload_mod_for_state(lua_State *L) -> void
### auto execute_repl(lua_State *L, const std::string &code) -> void
### auto request_table_expand(const std::string &path) -> void
### auto render() -> void
### auto get() -> LuaDebugger &
### auto has_instance() -> bool
### auto get_stack_slots(lua_State *L) -> std::vector< LuaStackSlot >
### auto get_call_stack(lua_State *L) -> std::vector< LuaCallStackEntry >
### auto get_stack_frames_with_locals(lua_State *L) -> std::vector< LuaStackFrame >
### auto format_stack_value(lua_State *L, int index, size_t max_length=MAX_STACK_PREVIEW_LENGTH) -> std::string
### auto get_enhanced_traceback(lua_State *L, const std::string &message, int level=0) -> std::string
### auto get_globals(lua_State *L, size_t max_entries=100) -> std::vector< std::pair< std::string, LuaStackSlot > >
### auto debug_hook(lua_State *L, lua_Debug *ar) -> void
### auto get_table_children(lua_State *L, const std::string &path, int depth=0) -> std::vector< LuaValueNode >

# RC::UE4SSProgram

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/UE4SSProgram.hpp`
Kind: class

## Members

### enum IsInstalled

- `Yes`
- `No`
### enum IsStarted

- `Yes`
- `No`
### variable constexpr CharType m_settings_file_name
### variable constexpr CharType m_log_file_name
### variable constexpr CharType m_object_dumper_file_name
### variable SettingsManager settings_manager
### variable bool unreal_is_shutting_down
### variable std::atomic_bool cpp_mods_done_loading
### variable UE4SSProgram * s_program
### variable bool m_is_program_started
### variable std::jthread m_render_thread
### variable std::vector< std::unique_ptr< Mod > > m_mods
### variable RecognizableStruct m_shared_functions
### variable bool m_has_game_specific_config
### variable bool m_processing_events
### variable bool m_pause_events_processing
### variable bool m_custom_member_variable_layout_loaded
### UE4SSProgram(const std::filesystem::path &ModuleFilePath, std::initializer_list< BinaryOptions > options)
### ~UE4SSProgram()
### UE4SSProgram(const UE4SSProgram &)=delete
### UE4SSProgram(UE4SSProgram &&)=delete
### auto init() -> void
### auto is_program_started() -> bool
### auto find_mod_by_id(ModId mod_id) -> Mod *
### auto find_lua_mod_by_id(ModId mod_id) -> LuaMod *
### auto queue_reinstall_mods() -> void
### auto queue_reinstall_mod(LuaMod *mod) -> void
### auto queue_reinstall_mod(ModId mod_id) -> void
### auto queue_uninstall_mod(LuaMod *mod) -> void
### auto queue_uninstall_mod(ModId mod_id) -> void
### auto queue_reinstall_mod_by_name(const std::string &mod_name) -> void
### auto queue_reinstall_mod_by_name(std::string_view mod_name) -> void
### auto queue_uninstall_mod_by_name(const std::string &mod_name) -> void
### auto queue_uninstall_mod_by_name(std::string_view mod_name) -> void
### auto queue_start_lua_mod_by_path(const std::filesystem::path &mod_path) -> void
### auto get_object_dumper_output_directory() -> const File::StringType
### auto get_module_directory() -> File::StringType
### auto get_game_executable_directory() -> File::StringType
### auto get_working_directory() -> File::StringType
### auto get_mods_directory() -> File::StringType
### auto get_mods_directories() -> std::vector< std::filesystem::path > &
### auto get_mods_txt_entries() -> std::unordered_map< std::string, bool >
### auto make_compatible_path(const std::filesystem::path &) const -> std::filesystem::path
### auto insert_mods_directory(const std::filesystem::path &, int64_t index) -> void
### auto add_mods_directory(const std::filesystem::path &) -> void
### auto remove_mods_directory(const std::filesystem::path &) -> void
### auto get_legacy_root_directory() -> File::StringType
### auto generate_uht_compatible_headers() -> void
### auto generate_cxx_headers(const std::filesystem::path &output_dir) -> void
### auto generate_lua_types(const std::filesystem::path &output_dir) -> void
### auto get_debugging_ui() -> GUI::DebuggingGUI &
### auto stop_render_thread() -> void
### auto add_gui_tab(std::shared_ptr< GUI::GUITab > tab) -> void
### auto remove_gui_tab(std::shared_ptr< GUI::GUITab > tab) -> void
### auto queue_event(EventCallable callable) -> void
### auto queue_event(LegacyEventCallable callable, void *data) -> void
### auto is_queue_empty() -> bool
### auto can_process_events() -> bool
### auto get_event_loop_thread_id() const -> std::thread::id
### auto is_event_loop_thread() -> bool
### auto delete_mod(Mod *) -> void
### auto register_keydown_event(Input::Key, const Input::EventCallbackCallable &, uint8_t custom_data=0, void *custom_data2=nullptr) -> void
### auto register_keydown_event(Input::Key, const Input::Handler::ModifierKeyArray &, const Input::EventCallbackCallable &, uint8_t custom_data=0, void *custom_data2=nullptr) -> void
### auto is_keydown_event_registered(Input::Key) -> bool
### auto is_keydown_event_registered(Input::Key, const Input::Handler::ModifierKeyArray &) -> bool
### auto get_all_input_events(std::function< void(Input::KeySet &)> callback) -> void
### auto find_mod_by_name(StringViewType mod_name, IsInstalled is_installed, IsStarted is_started) -> LuaMod *
### auto find_mod_by_name(StringViewType mod_name, IsInstalled is_installed, IsStarted is_started) -> CppMod *
### auto find_mod_by_name(std::string_view mod_name, IsInstalled is_installed, IsStarted is_started) -> LuaMod *
### auto find_mod_by_name(std::string_view mod_name, IsInstalled is_installed, IsStarted is_started) -> CppMod *
### auto get_current_imgui_context() -> ImGuiContext *
### auto get_current_imgui_allocator_functions(ImGuiMemAllocFunc *alloc_func, ImGuiMemFreeFunc *free_func, void **user_data) -> void
### auto dump_uobject(Unreal::UObject *object, std::unordered_set< Unreal::FField * > *dumped_fields, StringType &out_line, bool is_below_425, std::unordered_set< Unreal::UFunction * > *in_dumped_functions=nullptr) -> void
### auto dump_all_objects_and_properties(const File::StringType &output_path_and_file_name) -> void
### auto find_mod_by_name(StringViewType mod_name, IsInstalled=IsInstalled::No, IsStarted=IsStarted::No) -> T *
### auto find_mod_by_name(std::string_view mod_name, IsInstalled=IsInstalled::No, IsStarted=IsStarted::No) -> T *
### auto find_lua_mod_by_name(StringViewType mod_name, IsInstalled=IsInstalled::No, IsStarted=IsStarted::No) -> LuaMod *
### auto find_lua_mod_by_name(std::string_view mod_name, IsInstalled=IsInstalled::No, IsStarted=IsStarted::No) -> LuaMod *
### auto static_cleanup() -> void
### auto get_program() -> UE4SSProgram &
### auto parse_semicolon_separated_string(const StringType &string) -> std::vector< StringType >

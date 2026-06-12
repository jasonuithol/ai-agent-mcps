# RC::GUI

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/BPMods.hpp`
Kind: namespace

## Members

### enum GfxBackend

- `DX11`
- `GLFW3_OpenGL3`
### enum RenderMode

- `ExternalThread`
- `EngineTick`
- `GameViewportClientTick`
### enum OSBackend

- `Windows`
### variable ImColor g_imgui_bg_color
### variable ImColor g_imgui_text_color
### variable ImColor g_imgui_text_inactive_color
### variable ImColor g_imgui_text_editor_default_bg_color
### variable ImColor g_imgui_text_editor_default_text_color
### variable ImColor g_imgui_text_editor_normal_bg_color
### variable ImColor g_imgui_text_editor_normal_text_color
### variable ImColor g_imgui_text_editor_verbose_bg_color
### variable ImColor g_imgui_text_editor_verbose_text_color
### variable ImColor g_imgui_text_editor_warning_bg_color
### variable ImColor g_imgui_text_editor_warning_text_color
### variable ImColor g_imgui_text_editor_error_bg_color
### variable ImColor g_imgui_text_editor_error_text_color
### variable ImColor g_imgui_text_live_view_unreflected_data_color
### variable ImColor g_imgui_text_green_color
### variable ImColor g_imgui_text_blue_color
### variable ImColor g_imgui_text_purple_color
### auto render_mode_to_string(RenderMode mode) -> std::string
### auto gui_thread(std::optional< std::stop_token > stop_token, DebuggingGUI *debugging_ui) -> void
### auto TRY(CodeToTry code_to_try)
### auto scaled(float value) -> float
### auto ImGui_AutoScroll(const char *label, float *previous_max_scroll_y) -> void
### auto ImGui_InputTextMultiline_WithAutoScroll(const char *label, char *buf, size_t buf_size, const ImVec2 &size=ImVec2(0, 0), ImGuiInputTextFlags flags=0, ImGuiInputTextCallback callback=0, void *user_data=0, float *previous_max_scroll_y=nullptr)
### auto ImGui_Splitter(bool split_vertically, float thickness, float *size1, float *size2, float min_size1, float min_size2, float splitter_long_axis_size=-1.0f) -> bool
### auto ImGui_GetID(int int_id) -> ImGuiID
### auto ImGui_TreeNodeEx(const char *label, int int_id, ImGuiTreeNodeFlags flags=0) -> bool
### auto ImGui_TreeNodeEx(const char *label, void *ptr_id, ImGuiTreeNodeFlags flags=0) -> bool
### auto ImGui_TreeNodeEx(const char *label, const char *str_id, ImGuiTreeNodeFlags flags) -> bool
### auto is_player_controlled(UObject *object) -> bool
### auto ufunction_caller_search_mode_changed(void *userdata, SearcherWidget::SearchMode) -> void
### auto ufunction_caller_all_iterator(void *userdata) -> void
### auto ufunction_caller_search_iterator(void *userdata) -> void

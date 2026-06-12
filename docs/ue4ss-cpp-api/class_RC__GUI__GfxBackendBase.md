# RC::GUI::GfxBackendBase

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/GUI.hpp`
Kind: class

## Members

### GfxBackendBase()=default
### ~GfxBackendBase()=default
### auto set_os_backend(OSBackendBase *backend)
### auto init() -> void=0
### auto imgui_backend_newframe() -> void=0
### auto render(const float clear_color_with_alpha[4]) -> void=0
### auto shutdown() -> void=0
### auto cleanup() -> void=0
### auto create_device() -> bool=0
### auto cleanup_device() -> void=0
### auto handle_window_resize(int64_t param_1, int64_t param_2) -> void=0
### auto on_os_backend_set() -> void=0
### auto get_window_size() -> WindowSize
### auto get_window_position() -> WindowPosition
### auto exit_requested() -> bool

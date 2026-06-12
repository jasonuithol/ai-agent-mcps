# RC::GUI::OSBackendBase

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/GUI.hpp`
Kind: class

## Members

### OSBackendBase()=default
### ~OSBackendBase()=default
### auto set_gfx_backend(GfxBackendBase *backend)
### auto is_valid() -> bool
### auto init() -> void=0
### auto imgui_backend_newframe() -> void=0
### auto create_window(int loc_x=100, int loc_y=100, int size_x=1280, int size_y=800) -> void=0
### auto exec_message_loop(bool *exit_requested) -> void=0
### auto shutdown() -> void=0
### auto cleanup() -> void=0
### auto get_window_handle() -> void *=0
### auto get_window_size() -> WindowSize=0
### auto get_window_position() -> WindowPosition=0
### auto on_gfx_backend_set() -> void=0

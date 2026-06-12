# RC::GUI::DebuggingGUI

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/GUI.hpp`
Kind: class

## Members

### typedef std::function< void()> EndOfFrameCallback
### variable bool m_event_thread_busy
### DebuggingGUI()=default
### ~DebuggingGUI()
### auto is_valid() const -> bool
### auto is_open() const -> bool
### auto set_open(bool new_open) -> void
### auto exit_requested() const -> bool
### auto request_exit() -> void
### auto setup(std::stop_token *token) -> void
### auto get_console() -> Console &
### auto get_live_view() -> LiveView &
### auto set_gfx_backend(GfxBackend) -> void
### auto add_tab(std::shared_ptr< GUITab > tab) -> void
### auto remove_tab(std::shared_ptr< GUITab > tab) -> void
### auto uninitialize() -> void
### auto main_loop_internal() -> void
### auto execute_at_end_of_frame(EndOfFrameCallback callback) -> void

# RC::GUI::LiveView::Watch

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/LiveView.hpp`
Kind: struct

## Members

### enum AcquisitionMethod

- `StaticFindObject`
- `FindFirstOf`
### enum Type

- `Property`
- `Function`
### variable std::mutex s_watch_lock
### variable Output::Targets< Output::FileDevice > output
### variable FProperty * property
### variable UObject * container
### variable StringType object_name
### variable StringType property_name
### variable StringType property_value
### variable size_t hash
### variable std::string history
### variable float history_previous_max_scroll_y
### variable AcquisitionMethod acquisition_method
### variable bool write_to_file
### variable bool show_history
### variable bool load_on_startup
### variable bool was_stop_load_on_startup_requested
### variable bool enabled
### variable bool function_is_hooked
### variable std::pair< int, int > function_hook_ids
### Watch()=delete
### Watch(StringType &&object_name, StringType &&property_name)

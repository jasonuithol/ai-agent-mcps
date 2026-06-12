# RC::GUI::LiveView

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/LiveView.hpp`
Kind: class

## Members

### enum UseIndex

- `Yes`
- `No`
### enum ContainerType

- `Object`
- `Array`
- `Struct`
### typedef void(LiveView::*)(int32_t, int32_t, const std::function< void(UObject *)> &) ObjectIteratorCallable
### variable std::vector< ObjectOrProperty > s_object_view_history
### variable size_t s_currently_selected_object_index
### variable std::unordered_map< UObject *, std::vector< size_t > > s_history_object_to_index
### variable std::vector< UObject * > s_name_search_results
### variable std::unordered_set< UObject * > s_name_search_results_set
### variable std::string s_name_to_search_by
### variable std::vector< std::unique_ptr< Watch > > s_watches
### variable std::unordered_map< WatchIdentifier, Watch * > s_watch_map
### variable std::unordered_map< void *, std::vector< Watch * > > s_watch_containers
### variable bool s_include_inheritance
### variable bool s_apply_search_filters_when_not_searching
### variable bool s_create_listener_removed
### variable bool s_delete_listener_removed
### variable bool s_selected_item_deleted
### variable bool s_need_to_filter_out_properties
### variable bool s_watches_loaded_from_disk
### variable bool s_filters_loaded_from_disk
### variable bool s_use_regex_for_search
### variable bool s_search_by_address
### LiveView()
### ~LiveView()
### auto set_is_searching_by_name(bool new_value) -> void
### auto set_search_field_clear_requested(bool new_value) -> void
### auto was_search_field_clear_requested() -> bool
### auto was_search_field_cleared() -> bool
### auto set_search_field_cleared(bool new_value) -> void
### auto set_listeners() -> void
### auto unset_listeners() -> void
### auto initialize() -> void
### auto render() -> void
### auto render_watches() -> void
### auto process_watches() -> void
### auto set_listeners_allowed(bool new_value) -> void
### auto are_listeners_allowed() -> bool
### auto process_property_watch(Watch &watch) -> void
### auto process_function_pre_watch(Unreal::UnrealScriptFunctionCallableContext &context, void *) -> void
### auto process_function_post_watch(Unreal::UnrealScriptFunctionCallableContext &context, void *) -> void

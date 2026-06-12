# RC::GUI::SearcherWidget

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/SearcherWidget.hpp`
Kind: class

## Members

### enum SearchMode

- `All`
- `ByName`
### typedef void(*)(void *userdata) IteratorCallback
### typedef void(*)(void *userdata, SearchMode) SearchModeChangedCallback
### SearcherWidget()=delete
### SearcherWidget(SearchModeChangedCallback, IteratorCallback all_iterator, IteratorCallback search_iterator, void *userdata=nullptr)
### auto render() -> void
### auto was_search_requested() -> bool
### auto get_search_value() -> const std::string &

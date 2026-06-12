# RC::GUI::Filter

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/GUI/LiveView/Filter/ClassNamesFilter.hpp`
Kind: namespace

## Members

### typedef bool FilterResult
### variable std::unordered_set< FProperty * > s_highlighted_properties
### auto is_highlighted(FProperty *property) -> bool
### auto highlight(FProperty *property) -> void
### auto eval_pre_search_filters(T &, UObject *object) -> FilterResult
### auto eval_pre_search_filters(Types< T, Ts... > &, UObject *object) -> FilterResult
### auto eval_post_search_filters(T &, UObject *object) -> FilterResult
### auto eval_post_search_filters(Types< T, Ts... > &, UObject *object) -> FilterResult
### auto is_instance(UObject *object, bool care_about_cdo=true) -> bool

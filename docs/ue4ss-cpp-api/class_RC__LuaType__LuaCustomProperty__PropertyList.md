# RC::LuaType::LuaCustomProperty::PropertyList

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaCustomProperty.hpp`
Kind: class

## Members

### typedef std::function< bool(LuaCustomProperty const &)> ForEachCallable
### auto add(StringType property_name, std::unique_ptr< Unreal::CustomProperty >) -> void
### auto clear() -> void
### auto for_each(Unreal::UObject *base, const ForEachCallable &callable) -> bool
### auto find_or_nullptr(Unreal::UObject *base, StringType property_name) -> Unreal::FProperty *

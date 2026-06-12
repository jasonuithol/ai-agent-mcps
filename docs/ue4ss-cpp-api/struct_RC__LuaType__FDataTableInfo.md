# RC::LuaType::FDataTableInfo

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaUDataTable.hpp`
Kind: struct

## Members

### variable Unreal::UDataTable * data_table
### variable Unreal::UScriptStruct * row_struct
### variable Unreal::FName row_struct_fname
### variable size_t row_size
### FDataTableInfo(Unreal::UDataTable *table)
### void validate_row_struct(const LuaMadeSimple::Lua &lua)
Validates that the DataTable has a valid row struct.
Throws if row struct is not found lua Lua state to throw against.

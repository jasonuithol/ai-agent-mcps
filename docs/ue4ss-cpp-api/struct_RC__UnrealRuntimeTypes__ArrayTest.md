# RC::UnrealRuntimeTypes::ArrayTest

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaCustomMemberFunctions.hpp`
Kind: struct

## Members

### typedef bool(*)(int) FuncParamType
### typedef bool(* FuncParamTypedef
### variable size_t ElementSize
### variable size_t ElementMinAlignment
### variable std::string TypeName
### variable FArrayProperty * Property
### variable bool TypeIsAlwaysPointer
### ArrayTest()
### ArrayTest(FScriptArray *ScriptArray, size_t ElementSize, size_t ElementMinAlignment, const std::string &TypeName, bool TypeIsAlwaysPointer, FArrayProperty *Property=nullptr)
### ArrayTest(FScriptArray &&ScriptArray, size_t ElementSize, size_t ElementMinAlignment, const std::string &TypeName, bool TypeIsAlwaysPointer, FArrayProperty *Property=nullptr)
### ArrayTest(ArrayTest &&From)
### ~ArrayTest()
### FScriptArray * GetScriptArray()
### auto Num() -> int32
### auto Max() -> int32
### auto FuncTestOne(bool(*func_param)(int)) -> void
### auto FuncTestTwo(FuncParamType func_param) -> void
### auto FuncTestThree(FuncParamTypedef func_param) -> void
### auto FuncTestFour(std::function< bool(int)> func_param) -> void
### auto ForEach(LoopAction(*Callable)(int Index, void *Element)) -> void
### auto GetElementAtIndex(int32 index) -> void *

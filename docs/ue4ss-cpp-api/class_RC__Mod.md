# RC::Mod

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/Mod/Mod.hpp`
Kind: class

## Members

### enum IsTrueMod

- `Yes`
- `No`
### variable UE4SSProgram & m_program
### Mod(UE4SSProgram &, StringType &&mod_name, std::filesystem::path &&mod_path)
### ~Mod()=default
### auto get_id() const -> ModId
### auto get_name() const -> StringViewType
### auto get_path() const -> const std::filesystem::path &
### auto start_mod() -> void=0
### auto uninstall() -> void=0
### auto set_installable(bool) -> void
### auto is_installable() const -> bool
### auto set_installed(bool) -> void
### auto is_installed() const -> bool
### auto is_started() const -> bool
### auto get_program() -> UE4SSProgram &
### auto get_program() const -> const UE4SSProgram &
### auto fire_update() -> void
### auto fire_unreal_init() -> void
### auto fire_ui_init() -> void
### auto fire_program_start() -> void
### auto update_async() -> void

# Vibe Coding

Provider-neutral skills packaged as independently installable plugins for coding
agents. Codex and Claude Code can install them globally for your user.

| Plugin | Included skills | Purpose |
|--------|-----------------|---------|
| [cpp-dev](plugins/cpp-dev/) | [cpp-style](plugins/cpp-dev/skills/cpp-style/SKILL.md) | Clean Code, C++ Core Guidelines, pointer contracts and lifetimes |
| [dev-workflow](plugins/dev-workflow/) | [canon-tdd](plugins/dev-workflow/skills/canon-tdd/SKILL.md) | Scenario-driven Canon TDD |
| [doc-tools](plugins/doc-tools/) | [text-writing](plugins/doc-tools/skills/text-writing/SKILL.md), [uml-diagrams](plugins/doc-tools/skills/uml-diagrams/SKILL.md) | Clear prose and focused diagrams: sequence, object, class, architecture/component, and activity/workflow |

Each plugin contains a portable `plugin.json`, Codex and Claude compatibility
manifests, and a `skills/` directory. References, templates, previews and licences
stay inside their skill packages. Instructions do not depend on a model provider;
discovery and available tools depend on the host.

## Layout

```text
plugins/
  cpp-dev/
  dev-workflow/
  doc-tools/
    plugin.json
    .codex-plugin/plugin.json
    .claude-plugin/plugin.json
    skills/
      text-writing/
      uml-diagrams/
.agents/plugins/marketplace.json # Codex catalog
.claude-plugin/marketplace.json  # Claude catalog
```

Both catalogs expose the three packages as the `vibe-coding` marketplace. Their
package paths resolve from this repository's root. Plugins contain their actual
files, so installed skills do not depend on a dotfiles checkout.

## Install

Install Git and the agent clients you use, then add this public marketplace.
Choose either or both clients and install the plugins you want.

### Codex

```sh
codex plugin marketplace add expiracy/vibe-coding
codex plugin add cpp-dev@vibe-coding
codex plugin add dev-workflow@vibe-coding
codex plugin add doc-tools@vibe-coding
```

### Claude Code

```sh
claude plugin marketplace add expiracy/vibe-coding
claude plugin install --scope user cpp-dev@vibe-coding
claude plugin install --scope user dev-workflow@vibe-coding
claude plugin install --scope user doc-tools@vibe-coding
```

Restart the clients after installation. Plugin names namespace their skills;
for example, Claude exposes `/cpp-dev:cpp-style`.

For another host, supply the same plugin or skill packages through its supported
loading mechanism. Plugin installation does not install a C++ or LaTeX toolchain.

## Update or develop plugins

Refresh the marketplace with `codex plugin marketplace upgrade vibe-coding` or
`claude plugin marketplace update vibe-coding`. Install the desired Codex package
with `codex plugin add <name>@vibe-coding`, or update a Claude package with
`claude plugin update <name>@vibe-coding`. Restart the client to load changes.

For local development, pass the checkout path to each client's
`plugin marketplace add` command instead of `expiracy/vibe-coding`.
Edit a skill within its plugin's `skills/` directory. When releasing a plugin
change, update its version in the portable, Codex and Claude manifests together,
then commit and push.

## Migrating from the dotfiles marketplace

Install the replacements from `vibe-coding` first. Then remove the old
installations and marketplace in each client you configured.

```sh
codex plugin remove cpp-dev@expiracy-dotfiles
codex plugin remove dev-workflow@expiracy-dotfiles
codex plugin remove doc-tools@expiracy-dotfiles
codex plugin marketplace remove expiracy-dotfiles
```

```sh
claude plugin uninstall --scope user --keep-data cpp-dev@expiracy-dotfiles
claude plugin uninstall --scope user --keep-data dev-workflow@expiracy-dotfiles
claude plugin uninstall --scope user --keep-data doc-tools@expiracy-dotfiles
claude plugin marketplace remove --scope user expiracy-dotfiles
```

The skill content and existing licences were preserved when moving these
packages from [dotfiles](https://github.com/expiracy/dotfiles).
Shared global `AGENTS.md` instructions and chezmoi configuration remain in that
repository; they are maintained separately from these plugins.

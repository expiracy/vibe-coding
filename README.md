# Vibe Coding

Provider-neutral skills packaged as independently installable plugins for coding
agents. Codex and Claude Code can install them globally for your user.

| Plugin | Included skills | Purpose |
|--------|-----------------|---------|
| [cpp-dev](plugins/cpp-dev/) | [clean-code](plugins/cpp-dev/skills/clean-code/SKILL.md), [cpp-guidelines](plugins/cpp-dev/skills/cpp-guidelines/SKILL.md) | Upstream Clean Code illustrated in C++, plus separate C++ language/library guidance |
| [java-dev](plugins/java-dev/) | [clean-code](plugins/java-dev/skills/clean-code/SKILL.md) | The same upstream Clean Code rules illustrated in Java |
| [dev-architecture](plugins/dev-architecture/) | [clean-architecture](plugins/dev-architecture/skills/clean-architecture/SKILL.md) | Policy boundaries, dependency direction and infrastructure isolation |
| [dev-workflow](plugins/dev-workflow/) | [canon-tdd](plugins/dev-workflow/skills/canon-tdd/SKILL.md), [test-strategy](plugins/dev-workflow/skills/test-strategy/SKILL.md) | Scenario-driven TDD and risk-based verification coverage |
| [doc-tools](plugins/doc-tools/) | [text-writing](plugins/doc-tools/skills/text-writing/SKILL.md), [uml-diagrams](plugins/doc-tools/skills/uml-diagrams/SKILL.md) | Clear prose and focused diagrams: sequence, object, class, architecture/component, and activity/workflow |

Each plugin contains a portable `plugin.json`, Codex and Claude compatibility
manifests, and a `skills/` directory. References, templates, previews and licences
stay inside their skill packages. Instructions do not depend on a model provider;
discovery and available tools depend on the host.

## Layout

```text
plugins/
  cpp-dev/
    skills/
      clean-code/
      cpp-guidelines/
  java-dev/
    skills/clean-code/
  dev-architecture/
    skills/clean-architecture/
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

Both catalogs expose the five packages as the `vibe-coding` marketplace. Their
package paths resolve from this repository's root. Plugins contain their actual
files, so installed skills do not depend on a dotfiles checkout.

## Install

Install Git and the agent clients you use, then add this public marketplace.
Choose either or both clients and install the plugins you want.

### Codex

```sh
codex plugin marketplace add expiracy/vibe-coding
codex plugin add cpp-dev@vibe-coding
codex plugin add java-dev@vibe-coding
codex plugin add dev-architecture@vibe-coding
codex plugin add dev-workflow@vibe-coding
codex plugin add doc-tools@vibe-coding
```

### Claude Code

```sh
claude plugin marketplace add expiracy/vibe-coding
claude plugin install --scope user cpp-dev@vibe-coding
claude plugin install --scope user java-dev@vibe-coding
claude plugin install --scope user dev-architecture@vibe-coding
claude plugin install --scope user dev-workflow@vibe-coding
claude plugin install --scope user doc-tools@vibe-coding
```

Restart the clients after installation. Plugin names namespace their skills;
for example, Claude exposes `/cpp-dev:clean-code` and `/cpp-dev:cpp-guidelines`.

For another host, supply the same plugin or skill packages through its supported
loading mechanism. Plugin installation does not install a C++, Java or LaTeX toolchain.

## Clean Code source and language variants

Both Clean Code skills are based directly on
[pproenca/dot-skills](https://github.com/pproenca/dot-skills/tree/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code)
at commit `cf93c57cac89d6fc3e4194686000411567f5caf3`, upstream version 1.0.7. They preserve its 48-rule,
ten-category collection and licence, with a concise main file and detailed
references. Each variant records its source and adaptation notes.

- `cpp-dev:clean-code` uses C++17 examples of the upstream principles.
- `java-dev:clean-code` retains/adapts the upstream Java examples for Java 11.
- `cpp-dev:cpp-guidelines` remains separate and unchanged: resources, pointers,
  lifetimes, object semantics, interfaces and other C++ implementation policies.

Choose the Clean Code variant for the project's language. A C++ task can also use
`cpp-guidelines` when implementation contracts matter. The Clean Code variants
are independent copies of the upstream material and do not depend on the user's
downstream fork or on each other.

## Clean Architecture

`dev-architecture:clean-architecture` is shared across languages. It adapts the
same upstream repository's 42-rule architecture collection, with a concise main
file, detailed references and matching C++17/Java 11 boundary examples. The
[source notes](plugins/dev-architecture/skills/clean-architecture/UPSTREAM.md)
record the pinned revision, licence and corrections.

Use it for module boundaries, dependency direction and separation of business
policy from infrastructure. Clean Code covers code-level clarity; C++ guidelines
cover language/library choices; Canon TDD covers the development cycle. Apply
only the skills relevant to the task. Simple work may need no new layers.

## Test strategy

`dev-workflow:test-strategy` chooses useful verification from a change's behavior
and risks: direct tests, integration and contract checks, critical end-to-end
journeys and relevant failure cases. Supporting references cover dependency
realism, partial success, independent expectations and honest execution reports.
The main skill stays concise and provider-neutral.

Canon TDD remains the separate implementation loop. Test strategy helps choose
coverage; TDD implements one selected scenario at a time. Existing frameworks and
project conventions govern the actual checks, with no fixed test ratios.

## Automatic skill context

The plugins include context-loading hooks for Codex and Claude Code. Relevant main
skill bodies load from task hints or source/document reads and edits, then remain
quiet on repeated operations. Active bodies are restored after compaction/resume;
detailed references stay on demand. This includes test strategy as well as TDD.

Python 3.9+ with a `python3` command is required for the hooks. After updating and
restarting, review/trust the Codex hook definitions through `/hooks`; installation
does not automatically trust them. See the
[loading policy, setup and limitations](docs/skill-context-hooks.md). The skills
remain usable in hosts without these hook adapters.

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

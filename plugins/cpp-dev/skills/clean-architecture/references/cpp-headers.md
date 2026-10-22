# C++ headers and architectural boundaries

For C++20 header creation, edits and review, check the contract callers see.
A small helper may need only a quick check; do not add layers or reorganize a
repository just because a header changed.

## Own the contract

Identify the consumers, policy and component owning the header. Public parameter
and return types, bases, template arguments and inline bodies create dependencies.
Keep SQL/HTTP/vendor representations outside policy contracts when they couple
policy to infrastructure. A consumer-owned port may be a function, callable,
template requirement or runtime interface; choose from actual substitution needs.

Avoid exposing private implementation, but also avoid duplicate DTOs and mapping
for calls with identical meanings and change reasons. Preserve API/ABI contracts.

## Check includes and build dependencies

- Include what the header itself needs; it should compile when included first.
  Follow the project's include-guard or pragma-once convention.
- Forward-declare only where incomplete types are valid. By-value members, bases
  and operations requiring a complete type need its definition. Removing an include
  does not remove semantic coupling to a type or reverse a dependency.
- Put non-template implementation in source files where useful; keep required
  template definitions visible using the established inclusion/module approach.
  Header definitions must satisfy the one-definition rule across translation units.
- Check include and CMake target cycles, including transitive public include/link
  requirements. An umbrella target can accidentally expose infrastructure to policy.
- Use PImpl or a facade when build isolation, ABI stability or hiding implementation
  justifies its cost. Neither is required for every class.

Ownership, dangling views, special members and parameter passing remain the job
of cpp-guidelines; this reference concerns the architectural contract.

## Verify the affected boundary

Compile a scratch translation unit including each changed public header first,
with the actual target flags, definitions and include paths. Build relevant
consumers; one header compile cannot prove API/ABI compatibility. Use a build
with multiple translation units when header definitions change. Run focused
behavior tests and real adapter/composition checks where affected, and distinguish
compile evidence from runtime guarantees in the report.

See [dependency direction](dep-inward-only.md), [interface ownership](dep-interface-ownership.md),
and [boundary cost](bound-boundary-cost-awareness.md).

---
title: Domain Layer Has Zero Framework Dependencies
impact: MEDIUM
impactDescription: enables framework migration, pure unit tests
tags: frame, domain, purity, dependencies
---

## Domain Layer Has Zero Framework Dependencies

Keep the domain independent of delivery frameworks, persistence mechanisms and vendor-specific data formats. Standard-library types and stable domain-supporting libraries can be appropriate; dependency direction and policy coupling matter more than a blanket ban on packages.

**Incorrect (domain depends on framework):**

```csharp
// Domain entity with framework dependencies
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace Domain.Entities
{
    [Table("products")]
    public class Product
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [MaxLength(100)]
        [JsonProperty("product_name")]
        public string Name { get; set; }

        [Column(TypeName = "decimal(18,2)")]
        public decimal Price { get; set; }

        // EF Core navigation property
        public virtual Category Category { get; set; }

        // Framework-specific validation
        public IEnumerable<ValidationResult> Validate(ValidationContext context)
        {
            if (Price < 0)
                yield return new ValidationResult("Price cannot be negative");
        }
    }
}
// Domain now depends on: EF Core, DataAnnotations, Newtonsoft.Json
// Cannot exist without these frameworks
```

**Correct (pure domain):**

```csharp
// Domain entity - zero framework dependencies
namespace Domain.Entities
{
    public class Product
    {
        public ProductId Id { get; }
        public string Name { get; private set; }
        public Money Price { get; private set; }
        public CategoryId CategoryId { get; private set; }

        public Product(ProductId id, string name, Money price, CategoryId categoryId)
        {
            if (string.IsNullOrWhiteSpace(name))
                throw new InvalidProductNameException();
            if (name.Length > 100)
                throw new ProductNameTooLongException(name.Length, 100);
            if (price.IsNegative)
                throw new NegativePriceException(price);

            Id = id;
            Name = name;
            Price = price;
            CategoryId = categoryId;
        }

        public void UpdatePrice(Money newPrice)
        {
            if (newPrice.IsNegative)
                throw new NegativePriceException(newPrice);
            Price = newPrice;
        }
    }
}

// Infrastructure - framework dependencies isolated here
namespace Infrastructure.Persistence
{
    using Microsoft.EntityFrameworkCore;

    [Table("products")]
    internal class ProductEntity
    {
        [Key] public int Id { get; set; }
        [MaxLength(100)] public string Name { get; set; }
        [Column(TypeName = "decimal(18,2)")] public decimal Price { get; set; }
        public int CategoryId { get; set; }
    }

    internal class ProductMapper
    {
        public Product ToDomain(ProductEntity entity) => /* ... */
        public ProductEntity ToEntity(Product product) => /* ... */
    }
}
```

**How to check domain purity:**
```bash
# Inspect domain package references for outward dependencies.
dotnet list Domain.csproj package
# Assess each dependency; an empty package list alone does not prove isolation.

# Or in package.json
# "dependencies": {} should be empty or only contain domain libraries
```

Reference: [Clean Architecture - Frameworks are Details](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [frame-domain-purity](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-domain-purity.md).

# -*- coding: utf-8 -*-
"""
Build all 50 articles and 5 category hub pages.
"""
import os
import scripts.build_portal_and_articles as builder
import scripts.additional_24_articles as new_arts

# Check existing
print(f"Existing articles in builder: {len(builder.ARTICLES)}")
print(f"New articles to add: {len(new_arts.NEW_ARTICLES)}")

# Check for slug collision
existing_slugs = set(a['slug'] for a in builder.ARTICLES)
for a in new_arts.NEW_ARTICLES:
    if a['slug'] in existing_slugs:
        print(f"WARNING: Slug collision detected: {a['slug']}")

# Append new articles to builder.ARTICLES
builder.ARTICLES.extend(new_arts.NEW_ARTICLES)
print(f"Total articles now: {len(builder.ARTICLES)}")

# Count per category
cat_counts = {}
for a in builder.ARTICLES:
    cat_counts[a['category']] = cat_counts.get(a['category'], 0) + 1

print("\nArticles per category:")
for cat, count in sorted(cat_counts.items()):
    print(f"  {cat}: {count} articles")

# Run build
print("\n--- Generating Guide Articles ---")
for art in builder.ARTICLES:
    file_path = os.path.join(builder.GUIDE_DIR, f"{art['slug']}.html")
    content = builder.render_article_html(art)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(builder.ARTICLES)} guide articles in {builder.GUIDE_DIR}/")

print("\n--- Generating Category Hub Pages ---")
for hub in builder.CATEGORY_HUBS:
    content = builder.render_category_hub_html(hub)
    with open(hub["slug"], "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated {hub['slug']}")

print("\nAll 50 articles and 5 category hubs generated successfully!")

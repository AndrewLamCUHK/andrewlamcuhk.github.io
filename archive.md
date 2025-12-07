---
layout: page
title: Blog Archive
---

{% assign total_words = 0 %}
{% assign total_posts = 0 %}

{% for tag in site.tags %}
<h3>{{ tag[0] }}</h3>
<ul>
  {% for post in tag[1] %}
    {% assign content = post.content | strip_html | strip_newlines %}
    {% assign words = content | size %}
    {% assign total_words = total_words | plus: words %}
    {% assign total_posts = total_posts | plus: 1 %}
  <li><a href="{{ post.url }}">{{ post.date | date: "%B %Y" }} - {{ post.title }}</a></li>
  {% endfor %}
</ul>
{% endfor %}

<hr>

<h3>📊 博客统计</h3>
<ul>
  <li><strong>总文章数</strong>: {{ total_posts }} 篇</li>
  <li><strong>总字数</strong>: {{ total_words }} 字</li>
  <li><strong>平均每篇</strong>: {{ total_words | divided_by: total_posts }} 字</li>
</ul>

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

<h3>小计</h3>
<ul>
  <li><发表了: {{ total_posts }} 篇文章</li>
  <li>总字数: {{ total_words }} 字</li>
  <li>平均每篇: {{ total_words | divided_by: total_posts }} 字</li>
</ul>

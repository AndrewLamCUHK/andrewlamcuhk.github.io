愿为五陵轻薄儿，生在贞观开元时。

斗鸡走犬过一生，天地安危两不知。


{% assign featured_posts = site.posts | where: "featured", true | sort: "date" %}
<section class="featured-posts">
  <h2>Featured posts</h2>
  <ul>
    {% for post in featured_posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      </li>
    {% endfor %}
  </ul>
</section>


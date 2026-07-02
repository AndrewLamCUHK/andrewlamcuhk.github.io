创建这个博客的时候，我坐在电脑前想了很久名字，最后选了这三个字：去哪吃。

这是个太朴素的名字，朴素到几乎不像一个博客的名字。它没有典故，没有隐喻，没有任何可以被"解读"的深意。它只是我们每天都要面对的一个问题。

去哪吃，是生活里最小单位的决策，却承载着某种近乎哲学的重量。它每天都要被回答，它是最诚实的自画像。一个人选择吃什么、去哪吃、和谁吃、吃多少，这些细碎的日常里藏着的，是一个人的性情、处境，以及他与这个世界相处的方式。

所以我用了这个名字。不是因为我想写一个美食博客，而是因为那些每天在去哪吃三个字里流淌过去的琐碎、犹豫、妥协与偶尔的惊喜，才是生活最本来的样子。


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



<div>{{data}}</div>
<div>
{% for x in data %}
<p>{{x.title}}</p>

<p>{{x.genre}}<p>
<button>
    Book</button>
{% endfor %}
</div>
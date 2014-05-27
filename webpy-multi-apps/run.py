import blog
import wiki
import delegate

mapping = (
    ("/blog", blog.urls, blog),
    ("/wiki", wiki.urls, wiki)
)

if __name__ == "__main__":
    delegate.run(mapping)
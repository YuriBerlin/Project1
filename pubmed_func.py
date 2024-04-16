
def get_pubmed(query, max_results=5):
    from pymed import PubMed
    pubmed = PubMed(tool="MyTool")
    results = pubmed.query(query, max_results)
    article_list=[]
    for article in results:
        print(f"Title: {article.title}")
        article_list.append(f"Title: {article.title}" + f"Abstract: {article.abstract}")
    return article_list


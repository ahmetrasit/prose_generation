# source_access.md — exact Quran passages on demand

Before developing a Quran cross-reference, retrieve its actual text and adjacent context. Use this command, replacing S:A,S:A with the references you need (up to 16 per request):

    python3 -B /Volumes/OZTURK/_projects/prose_generation/_commentary/v14/sources.py --tag sol-argument --ref 1:6 --refs S:A,S:A --context 1

The helper reads only the frozen Quran corpus and logs the returned references and bytes. It never calls a model. Context may be 0, 1, 2 or 3 ayat on each side; use further requests when a scene needs more context. Do not read the entire corpus or unrelated repository files. Copy Quran quotations from returned text or the normalized concordance. Retrieval is for checking and understanding the passages you develop, not for turning all candidates into obligatory quotations. The full preceding prose is reader context, not a quotation source.

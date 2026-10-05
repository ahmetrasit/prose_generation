"""Segment-level tradition and witness metadata for the separate Bible index."""

NT_BOOKS = set('Matt Mark Luke John Acts Rom 1Cor 2Cor Gal Eph Phil Col 1Thess 2Thess 1Tim 2Tim Titus Phlm Heb Jas 1Pet 2Pet 1John 2John 3John Jude Rev'.split())
OT_BOOKS = set('Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal'.split())
APOCRYPHA = set('Tob Jdt EsthGr Wis Sir Bar PrAzar Sus Bel 1Macc 2Macc 1Esd 2Esd PrMan AddPs EpJer'.split())


def metadata(sid: str, segment: dict) -> dict:
    """Conservative classification; unknown/background entries never become scripture."""
    if sid == 'WLC':
        return {'gelenek': ['tevrat'], 'nusha': ['masoretik'], 'versification': 'Bible.MT'}
    if sid == 'SBLGNT':
        return {'gelenek': ['incil'], 'nusha': ['yunanca_ahit'], 'versification': 'SBLGNT'}
    if sid == 'KJV':
        book = segment.get('book') or segment['seg'].split(':', 1)[1].split('.')[0]
        trad = ['incil'] if book in NT_BOOKS else ['tevrat'] if book in OT_BOOKS | APOCRYPHA else []
        return {'gelenek': trad, 'translation_aid': True, 'requires_original': book in OT_BOOKS | NT_BOOKS,
                'versification': 'KJV', 'nusha': ['tercume']}
    if sid == 'SEFARIA':
        cats = segment.get('categories') or []
        witness = 'targum' if 'Targum' in cats else 'rabbani'
        return {'gelenek': ['tevrat'], 'nusha': [witness], 'versification': 'Sefaria'}
    if sid == 'CORPUSCORANICUM-INTERTEXT':
        cat = ' / '.join(str(segment.get(k) or '') for k in ('supercategory', 'category'))
        if 'Hebräische Bibel' in cat:
            return {'gelenek': ['tevrat'], 'nusha': ['masoretik']}
        if 'Neues Testament' in cat:
            return {'gelenek': ['incil'], 'nusha': ['yunanca_ahit']}
        if 'Pseudepigraphen' in cat:
            return {'gelenek': ['tevrat'], 'nusha': ['apokrif']}
        if 'Talmud' in cat or 'Midrasch' in cat or 'jüdische Gebete' in cat:
            return {'gelenek': ['tevrat'], 'nusha': ['rabbani']}
        if 'Patristik' in cat or 'Christliche' in cat or 'christliche Gebete' in cat:
            witnesses = ['patristik', 'suryani'] if segment.get('language') == 'Syrisch' else ['patristik']
            return {'gelenek': ['incil'], 'nusha': witnesses}
        return {'gelenek': [], 'background_only': True}
    return {}

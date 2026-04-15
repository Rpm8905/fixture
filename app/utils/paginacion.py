def construir_links_paginacion(url_base, offset_actual, limit, total_registros):
    offset_primera_pagina   = 0
    offset_ultima_pagina    = max(0, total_registros - limit)
    offset_pagina_previa    = max(0, offset_actual - limit)
    offset_pagina_siguiente = offset_actual + limit

    def construir_url(offset):
        return f"{url_base}?_limit={limit}&_offset={offset}"

    links = {
        "_first": { "href": construir_url(offset_primera_pagina) },
        "_last":  { "href": construir_url(offset_ultima_pagina) }
    }

    if offset_actual > 0:
        links["_prev"] = { "href": construir_url(offset_pagina_previa) }

    if offset_pagina_siguiente < total_registros:
        links["_next"] = { "href": construir_url(offset_pagina_siguiente) }

    return links
from rest_framework.response import Response


def list_portfolio(query):
    queryset = query.filter_queryset(query.get_queryset())
    summary = {
        'details_count': queryset.filter(user_profile__name=query.kwargs['username']).count(),
    }
    if summary['details_count'] > 0:
        summary['status'] = "success"
    else:
        summary['status'] = "empty"
    page = query.paginate_queryset(queryset)
    if page is not None:
        serializer = query.get_serializer(page, many=True)
        data = {
            'summary': summary,
            'data': serializer.data
        }
        return query.get_paginated_response(data)

    serializer = query.get_serializer(queryset, many=True)
    data = {
        'summary': summary,
        'data': serializer.data
    }
    return Response(data)


def list_api_query(query):
    queryset = query.filter_queryset(query.get_queryset())
    summary = {
        'details_count': queryset.count(),
    }
    if summary['details_count'] > 0:
        summary['status'] = "success"
    else:
        summary['status'] = "empty"
    page = query.paginate_queryset(queryset)
    if page is not None:
        serializer = query.get_serializer(page, many=True)
        data = {
            'summary': summary,
            'data': serializer.data
        }
        return query.get_paginated_response(data)

    serializer = query.get_serializer(queryset, many=True)
    data = {
        'summary': summary,
        'data': serializer.data
    }
    return Response(data)

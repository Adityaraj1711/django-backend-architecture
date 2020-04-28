from rest_framework.response import Response
from rest_framework import status


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


def detail_api_query(query, request):
    serializer = query.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    query.perform_create(serializer)
    headers = query.get_success_headers(serializer.data)
    summary = {}
    if status.HTTP_201_CREATED:
        summary['status'] = 'success'
        summary['statusCode'] = status.HTTP_201_CREATED
    else:
        summary['status'] = 'error'
        summary['statusCode'] = status.HTTP_400_BAD_REQUEST
    data = {
        'summary': summary,
        'data': serializer.data
    }

    return Response(data, status=status.HTTP_201_CREATED, headers=headers)

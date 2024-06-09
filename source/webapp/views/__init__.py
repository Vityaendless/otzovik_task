from .products_views import IndexView, ProductCreateView, ProductView, ProductUpdateView, ProductDeleteView
from .reviews_views import (ReviewCreateView, ReviewUpdateView, ReviewDeleteView, NoModerateReviewsView,
                            ReviewAcceptView, ReviewDeclineView)
from .errors_views import permission_denied

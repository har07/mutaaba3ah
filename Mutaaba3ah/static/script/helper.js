function calculateTotalPages(pageFrom, pageTo) {
    var total = 0;
    if (pageFrom > pageTo) {
        total = 604 - pageFrom + 1;
        total += pageTo;
    }
    else {
        total = pageTo - pageFrom + 1;
    }
    return total;
}
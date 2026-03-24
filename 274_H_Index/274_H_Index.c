/**
 * @author CodeamonCat/CodeamonCat@gmail.com
 */

int hIndex(int* citations, int citationsSize) {
    int *count = (int *)calloc(citationsSize + 1, sizeof(int));

    for(int i = 0; i < citationsSize; i++) {
        if(citations[i] >= citationsSize) {
            count[citationsSize]++;
        } else {
            count[citations[i]]++;
        }
    }

    int h_val = 0;
    for(int i = citationsSize; i >= 0; i--) {
        h_val += count[i];
        if(h_val >= i) {
            free(count);
            return i;
        }
    }
    free(count);
    return 0;
}

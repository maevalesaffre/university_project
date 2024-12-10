#include <assert.h>
#include <stdio.h>
#include "logger.h"

static struct tlog_entry logs[MAX_LOGS];
static char errmsg[ERRMSG_LEN] = "";
/* index of the first free entry, and number of logged entries. To be
   accessed using atomic instructions */ 
static int log_index = 0;

tlog_entry tlog_s(char a, int b, int c)
{
    struct tlog_entry e = { .id = a, .n1 = b, .n2 = c};
    return e;
}

void tlog_log(char id, int n1, int n2)
{
    assert(id != '*' && n1 >= 0 && n2 >= 0);
    int index = __atomic_fetch_add(&log_index, 1, __ATOMIC_SEQ_CST);
    logs[index].id = id;
    logs[index].n1 = n1;
    logs[index].n2 = n2;
}

void tlog_clear()
{
    int val = 0;
    __atomic_store(&log_index, &val, __ATOMIC_SEQ_CST);
}

void tlog_print()
{
    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    for (int i=0; i<n; i++) {
        printf("%c(%d,%d)\n", logs[i].id, logs[i].n1, logs[i].n2);
    }
}

char *tlog_last_error_msg()
{
    return errmsg;
}

static int char_eq(char a, char b)
{
    if (a == '*' || b == '*') return 1;
    else return a == b;
}

static int int_eq(int a, int b)
{
    if (a < 0 || b < 0) return 1;
    else return a == b;
}

int tlog_cmp(struct tlog_entry *pa, struct tlog_entry *pb)
{
    if (char_eq(pa->id, pb->id) && int_eq(pa->n1, pb->n1) && int_eq(pa->n2, pb->n2))
        return 1;
    else return 0;
}

int tlog_exists(tlog_entry e)
{
    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    for (int i=0; i<n; i++)
        if (tlog_cmp(&e, &logs[i])) return 1;

    return 0;
}

int tlog_check_before(struct tlog_entry before, struct tlog_entry after)
{
    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    int i, j;
    int i_max = -1;
    int j_min = MAX_LOGS; 
    /* search for all "before" */
    for (i=0; i<n; i++) {
        if (tlog_cmp(&before, &logs[i])) i_max = i > i_max ? i : i_max;
    }
    
    /* search for all "after" */
    for (j=0; j<n; j++) {
        if (tlog_cmp(&after, &logs[j])) j_min = j < j_min ? j : j_min;
    }

    /* if any "before" comes after any "after", it's an error */ 
    if (i_max < j_min) return 1;
    else {
        sprintf(errmsg, "\033[1;31mError:\033[0m %c(%d,%d) after %c(%d,%d)\n",
                logs[j_min].id, logs[j_min].n1, logs[j_min].n2,
                logs[i_max].id, logs[i_max].n1, logs[i_max].n2);
        return 0;
    }
}

int tlog_check_all_n1(char id, int n1_min, int n1_max, int n2)
{
    assert(n1_min < n1_max);
    int c[n1_max - n1_min];
    for (int i=0; i<(n1_max-n1_min); i++) c[i] = 0;
    
    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    for (int i=0; i<n; i++)
        for (int x = n1_min; x<n1_max; x++) 
            if ((logs[i].id == id) && (logs[i].n1 == x) && (logs[i].n2 == n2)) {
                c[x-n1_min] = 1;
                break;
            }
    // TODO CHECK that all c are 1;
    for (int x=0; x<(n1_max - n1_min); x++)
        if (c[x] == 0) return 0;
    return 1;
}

int tlog_check_all_n2(char id, int n1, int n2_min, int n2_max)
{
    assert(n2_min < n2_max);
    int c[n2_max - n2_min];
    for (int i=0; i<(n2_max-n2_min); i++) c[i] = 0;
    
    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    for (int i=0; i<n; i++)
        for (int x = n2_min; x<n2_max; x++) 
            if ((logs[i].id == id) && (logs[i].n1 == n1) && (logs[i].n2 == x)) {
                c[x-n2_min] = 1;
                break;
            }
    // TODO CHECK that all c are 1;
    for (int x=0; x<(n2_max - n2_min); x++)
        if (c[x] == 0) return 0;
    return 1;
}

int tlog_check_seq_n2(char id, int n1, int n2_min, int n2_max)
{
    assert(n2_min < n2_max);
    int c[n2_max - n2_min];
    for (int i=0; i<(n2_max-n2_min); i++) c[i] = 0;

    int n = __atomic_load_n(&log_index, __ATOMIC_SEQ_CST);
    int i = 0;
    for (int x = n2_min; x<n2_max; x++) 
        while (i<n) {
            if ((logs[i].id == id) && (logs[i].n1 == n1) && (logs[i].n2 == x)) {
                c[x-n2_min] = 1;
                i++;
                break;
            }
            i++;
        }
    
    // TODO CHECK that all c are 1;
    for (int x=0; x<(n2_max - n2_min); x++)
        if (c[x] == 0) return 0;
    return 1;
}


from collections import deque

suggested_links = deque(map(int, input().split()))
featured_articles = [int(x) for x in input().split()]
target_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    first_el = suggested_links.popleft()
    second_el = featured_articles.pop()

    if second_el > first_el:
        dividend = second_el
        divisor = first_el
        remainder = dividend % divisor
        final_feed.append(remainder)
        remainder *= 2
        if remainder == 0:
            continue
        else:
            featured_articles.append(remainder)

    elif first_el == second_el:
        final_feed.append(first_el - second_el)
    else:
        dividend = first_el
        divisor = second_el
        remainder = dividend % divisor
        final_feed.append(-remainder)
        remainder *= 2
        if remainder == 0:
            continue
        else:
            suggested_links.append(remainder)

print(f"Final Feed: {', '.join(str(x) for x in final_feed)}")
total_value = sum(final_feed)
if total_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_value}")
else:
    print(f"Goal not achieved! Short by: {target_value - total_value}")

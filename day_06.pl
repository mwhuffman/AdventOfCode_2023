#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

##########
#
# time: 7
#
#  hold  remain  speed   travel
#  0 ms   7 ms  0 mm/ms   0 mm
#  1 ms   6 ms  1 mm/ms   6 mm
#  2 ms   5 ms  2 mm/ms  10 mm 
#  3 ms   4 ms  3 mm/ms  12 mm
#  4 ms   3 ms  4 mm/ms  12 mm
#  5 ms   2 ms  5 mm/ms  10 mm
#  6 ms   1 ms  6 mm/ms   6 mm
#  7 ms   0 ms  0 mm/ms   0 mm
#

my $file = "day_06.txt";

my @time_array;
my @dist_array;

open(FH, '<', $file) or die("Could not open file.");

while( my $row = <FH> ) {

    chomp($row);

    if ( $row =~ m/Time/ ) {
	 (my $name, my $array) = split(':', $row, 2);
	 chomp($array);
	 @time_array = split(' ', $array);
    } else {
	 (my $name, my $array) = split(':', $row, 2);
	 chomp($array);
	 @dist_array = split(' ', $array);
    }
    
}

close(FH);

# print Dumper @time_array;
# print Dumper @dist_array;

my $i = 0;
my @total_ways;
foreach my $game (@time_array) {
    my $ways = 0;
    for ( my $hold = 0; $hold <= $game; $hold++ ) {
	my $remain = $game - $hold;
	my $travel = $remain * $hold;
	if ( $travel > $dist_array[$i] ) {
	    print "Hold: $hold ms Remain: $remain ms Travel: $travel mm\n";
	    $ways++;
	}
    }
    $total_ways[$i] = $ways;
    $i++;
    print "ways: $ways\n";
}

print "total: $total_ways[0] $total_ways[1] $total_ways[2] $total_ways[3]\n";

my $total = $total_ways[0] * $total_ways[1] * $total_ways[2] * $total_ways[3];

print "total: $total\n";

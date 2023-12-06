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

my $time_array;
my $dist_array;

open(FH, '<', $file) or die("Could not open file.");

while( my $row = <FH> ) {

    chomp($row);

    if ( $row =~ m/Time/ ) {
	 (my $name, $time_array) = split(':', $row, 2);
	 $time_array =~ s/ //gi;
    } else {
	 (my $name, $dist_array) = split(':', $row, 2);
	 $dist_array =~ s/ //gi;
    }
    
}

close(FH);

print "time: $time_array\n";
print "dist: $dist_array\n";

my $ways = 0;
for ( my $hold = 0; $hold <= $time_array; $hold++ ) {
    my $remain = $time_array - $hold;
    my $travel = $remain * $hold;
    if ( $travel > $dist_array ) {
	# print "Hold: $hold ms Remain: $remain ms Travel: $travel mm\n";
	$ways++;
    }
}

print "total ways: $ways\n";

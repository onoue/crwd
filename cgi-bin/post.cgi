#!/usr/bin/perl
use strict;
use warnings;
use lib qw(../lib);
use MIME::Base64;
use JSON;
use CGI;

my $q = CGI->new;
my $id = $q->param('id');
my $raw_data = $q->param('data');
#my $data = decode_json($raw_data);


#add data to db.
sub add {
}


print $q->header;
print encode_json($raw_data);

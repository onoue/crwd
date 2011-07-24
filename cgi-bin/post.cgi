#!/usr/bin/perl
use strict;
use warnings;
use lib qw(../lib);
use MIME::Base64;
use JSON;
use CGI;
use LWP::Simple;

my $q = CGI->new;
my $word = $q->param('data');
#my $data = decode_json($raw_data);

my $content = get("http://eow.alc.co.jp/apple/UTF-8/");
die "Couldn't get it!" unless defined $content;
 
#add data to db.

print $q->header;
print encode_json($content);

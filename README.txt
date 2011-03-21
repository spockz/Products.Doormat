Introduction
============

A doormat is a large collection of links which are presented in a structured
way. One example is the current plone.org_, where the div#sitemap at the bottom
is actually an ordered collection of internal and external links, with sections
called "Downloads", "Documentation", "Developers", "Plone foundation" and
"Support". See more examples_ of doormats.

This product adds a couple of content types (Archetypes), which are used to
create a structure which is used for generating a doormat. A viewlet on this
doormat is placed in the Plone footer. The links in the Doormat are managed as
content, making the Doormat more flexible than a sitemap.  It's also possible
to add external links. It's also possible to add bits of text, with markup.


Getting started
===============

After installing the product in your site, you can add a "Doormat" item to your
Plone site. Inside it, you can create a hierarchical structure of Columns,
Sections, links (both internal and external), and Documents (Plone's Page type). 

The Doormat may look like this, schematically::

    +-- Doormat -----------------------------------------------------------------------+
    |                                                                                  |
    |  +-- Column 1 ----------+  +-- Column 2----------+  +-- Column 3 -------------+  |
    |  |                      |  |                     |  |                         |  |
    |  |  +-- Section 1 ----+ |  | +-- Section 1 ----+ |  | +-- Section 1 --------+ |  |
    |  |  |                 | |  | |                 | |  | |                     | |  |
    |  |  |  +-- Link 1 --+ | |  | |  +-- Link 1 --+ | |  | |  +-- Document 1 --+ | |  |
    |  |  |  +------------+ | |  | |  +------------+ | |  | |  |                | | |  |
    |  |  |                 | |  | |                 | |  | |  | (Contact info) | | |  |
    |  |  |  +-- Link 2 --+ | |  | |  +-- Link 2 --+ | |  | |  |                | | |  |
    |  |  |  +------------+ | |  | |  +------------+ | |  | |  +----------------+ | |  |
    |  |  |                 | |  | |                 | |  | |                     | |  |
    |  |  +-----------------+ |  | +-----------------+ |  | +---------------------+ |  |
    |  |                      |  |                     |  |                         |  |
    |  +----------------------+  +---------------------+  +-------------------------+  |
    |                                                                                  |
    +----------------------------------------------------------------------------------+

In fact, you can add more than one section, they will be displayed below each
other. In each section, you can mix internal links, external links and
Documents.

And in real life: 

.. image:: http://plone.org/products/doormat/screenshot

Note that the product adds an extra hierarchical layer compared to the
plone.org_ doormat: it adds a Column, which can contain more than one Section.
An example using this structure is the Oosterpoort_, which actually is the
product's predecessor.

Adding a Document
=================

Adding and editing a Document to the Doormat is just as simple as adding it in
any other place. However, keep this in mind that only the "Body text" field
will be displayed in the Doormat. Other fields, most notably the title and
description will be omitted.

Links in a Document
-------------------

By default, relative links will be created from the place where the Document
lives. This link is then displayed in the Doormat on all pages, so it is very
likely to be broken.

The solution is to make your editor insert links by uid. With TinyMCE on Plone
4, you can enable "link by uid" by going to the "Resource types" tab on TinyMCE
Settings (via the "Site setup"), and checking the box called "Link using UIDs". 

This will apply to the whole site. You may want to revert to the default
setting after you've added the link, as relative links are more desirable in
general.

Adding an Image
---------------

To add an image to the Doormat, add a Document and include an image there. It's
not possible to upload an Image to a DoormatSection, so you need to upload the
image to another place in your site first.

Make sure you enable "Link using UIDs" (see above) first, because defining the
image's location in a relative way will break in the same way as a relative
link will break.

Simple configuration
====================

You'll probably want to exclude the doormat object from navigation using the 
"Settings" tab. (This was not yet done when the above screenshot was taken.)

There's a field `showTitle` on the folderish types (Doormat, Column and
Section) which allows content managers to decide if the item's title should be
displayed in the doormat.


More advanced configuration and styling
=======================================

This section is intended for integrators and/or developers who would like to
customize the way the doormat is rendered in more detail.

Moving the doormat
------------------

By default, the default doormat viewlet (`doormat.footer`) is placed in the
`plone.portalfooter` viewlet manager. It's easy to modify this in an add-on
product, so the doormat will display below the global navigation (portal tabs),
or anywhere else in the site.


Displaying the doormat without the extra div elements
-----------------------------------------------------

The default viewlet renders the doormat inside Plone's default footer elements,
so it blends in with Plone 4's default Sunburst Theme::

  <div class="row">
    <div class="cell width-full position-0" >
      <div id="doormat-container" />
    </div>
  </div>

Using the `doormat.footer.bare` viewlet will omit the two outermost <div>'s.
This may be handy when using the doormat in a different theme, or in a
customized layout. You can hide the default viewlet and enable the bare version
through `@@manage-viewlets`, or by adding a customized `viewlets.xml` to the
product you're developing.


Caveats
=======

The viewlet does a catalog lookup for the `Doormat` portal type. If you have
more than one object of this type (nothing stops you), it will use the oldest
one.


Dependencies / Requirements
===========================

The product works on:

* Plone 3
* Plone 4


Credits
=======

This product was sponsored by GroningerForum_.


.. _examples: http://www.welie.com/patterns/showPattern.php?patternID=doormat
.. _plone.org: http://www.plone.org
.. _Oosterpoort: http://www.de-oosterpoort.nl
.. _GroningerForum: http://www.groningerforum.nl

PGDMP  5                	    |            prueba_django    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    52442    prueba_django    DATABASE        CREATE DATABASE prueba_django WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Peru.1252';
    DROP DATABASE prueba_django;
                postgres    false            �            1259    52444 	   categoria    TABLE     g   CREATE TABLE public.categoria (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL
);
    DROP TABLE public.categoria;
       public         heap    postgres    false            �            1259    52443    categoria_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categoria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.categoria_id_seq;
       public          postgres    false    216            �           0    0    categoria_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.categoria_id_seq OWNED BY public.categoria.id;
          public          postgres    false    215            �            1259    52451 	   productos    TABLE     �   CREATE TABLE public.productos (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text,
    stock integer,
    visibilidad boolean,
    categoria_id integer
);
    DROP TABLE public.productos;
       public         heap    postgres    false            �            1259    52450    productos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.productos_id_seq;
       public          postgres    false    218            �           0    0    productos_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;
          public          postgres    false    217                       2604    52447    categoria id    DEFAULT     l   ALTER TABLE ONLY public.categoria ALTER COLUMN id SET DEFAULT nextval('public.categoria_id_seq'::regclass);
 ;   ALTER TABLE public.categoria ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216                        2604    52454    productos id    DEFAULT     l   ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);
 ;   ALTER TABLE public.productos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            �          0    52444 	   categoria 
   TABLE DATA           /   COPY public.categoria (id, nombre) FROM stdin;
    public          postgres    false    216   �       �          0    52451 	   productos 
   TABLE DATA           ^   COPY public.productos (id, nombre, descripcion, stock, visibilidad, categoria_id) FROM stdin;
    public          postgres    false    218   m       �           0    0    categoria_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categoria_id_seq', 10, true);
          public          postgres    false    215            �           0    0    productos_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.productos_id_seq', 15, true);
          public          postgres    false    217            "           2606    52449    categoria categoria_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.categoria DROP CONSTRAINT categoria_pkey;
       public            postgres    false    216            $           2606    52458    productos productos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.productos DROP CONSTRAINT productos_pkey;
       public            postgres    false    218            %           2606    52459 %   productos productos_categoria_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_categoria_id_fkey FOREIGN KEY (categoria_id) REFERENCES public.categoria(id);
 O   ALTER TABLE ONLY public.productos DROP CONSTRAINT productos_categoria_id_fkey;
       public          postgres    false    218    216    4642            �   |   x�3�t�IM.):�9/39�ˈ3(� �˘�1'375�$��˄�#?=��˔�%� ��$��ˌ381�4E�R�)5''�*�˜�'3��ڂӫ4�4�ʒӱ�$?���� �Ѐ���b�-1z\\\ �'�      �   �  x�MS���0����q'�c�-���@;vad�!@I�,g��O�ر�[W�X����b�4��ǵ��<�99��az�?�d�0��Uz��ZT�����iz�������K�C�;��smL̍p`zh]%��T��+�<�z��&�tN���L��0z�D�KVr�����<���C*nՏ�AC%�M�ֈ�~���(2=z�pd,��^���v�F|�;ܝ4@��v35vD�q�jƶ��i��gJ�,�3\��}�>f��N�'M:�~�R�q6��
�`��D@�j��{4�>S�!@��(�qBm$95�%�x�p#���.�0��t"����4����bd��8���ŗ���aJ�;;?����<��.R[�|̈�f�;Y/�;�T�\����3r�3Y��K֚N�Tb�z<�z%��Ї��@�����ɤ�HrG���rS'0npw�.d��"�W�Z�( g�9�>�>�R�uy݈o�p`gqxp�x�j&��gg�>I���g%���*�     